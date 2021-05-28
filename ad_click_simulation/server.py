# Reference: https://www.udemy.com/bayesian-machine-learning-in-python-ab-testing
from __future__ import print_function, division
from builtins import range
import sys
import numpy as np
from flask import Flask, jsonify, request
from scipy.stats import beta

# create an app
app = Flask(__name__)


# define bandits
# there's no "pull arm" here
# since that's technically now the user/client
class Bandit:
  def __init__(self, name):
    self.name = name
    self.times = 1 #initialization for ucb only
    self.click = 0
    self.win_rate = 0

  def sample(self, totalViews):
    return self.win_rate + np.sqrt(2*np.log(totalViews)/self.times)

  def update_times(self):
    self.times+=1
    self.win_rate = ((self.times-1)*self.win_rate + 0)/self.times 
    return

  def update(self):
    self.click += 1
    self.win_rate = ((self.times-1)*self.win_rate + 1)/self.times 
    print("bandit: {}, view times: {}, click times: {}".format(self.name, self.times, self.click), file=sys.stderr)
    return

# initialization
banditA = Bandit('A')
banditB = Bandit('B')
total_views = 2 # initialization for ucb only, we assume both bandits have played once

bandit_dict = {0:'A', 1:'B'}
all_bandits = [banditA, banditB]


@app.route('/get_ad')
def get_ad():
  global total_views
  res = np.argmax([x.sample(total_views) for x in all_bandits])
  all_bandits[res].update_times()
  total_views += 1
  return jsonify({'advertisement_id': bandit_dict[res]})


@app.route('/click_ad', methods=['POST'])
def click_ad():
  result = 'OK'
  if request.form['advertisement_id'] == 'A':
    banditA.update()
  elif request.form['advertisement_id'] == 'B':
    banditB.update()
  else:
    result = 'Invalid Input.'

  # nothing to return really
  return jsonify({'result': result})


if __name__ == '__main__':
  app.run(host='127.0.0.1', port='8888')