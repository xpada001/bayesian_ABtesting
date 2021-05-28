# bayesian_ABtesting

## bayesian vs frequentist (a very general understanding)

In the frequentists' world, the result/parameters we are trying to find is fixed. The parameter is an unknown constant which could lie within a interval. Some popular techniques used by frequentists are maximum likelihood estimation, confidence interval and hypothesis testing

In bayesian methods, everything is a variable (i.e. have a distribution). The function of random variables is also random. To solve a problem, it would start with a prior distribution, which indicates the probability distribution of the unknown parameter before obtaining any data. The prior distribution would be updated based on the data collection, which would be called the posterior distribution.

## Frequentist A/B testing

In Frequentist A/B testing, we are using hypothesis testing and p-values to make a decision. For example, given two version A and B, we can set a null hypothesis that version A and B has the same impact. Then we can calculate the p-value accordingly. The p-value is the probability of obtaining results at least as extreme as the results we observed, provided that the null hypothesis is correct. Once we obtain a conclusion of statistical significance, the testing is completed. Usually, p-value < 0.05 indicates that we can reject the null hypothesis. Otherwise, we fail to reject the null hypothesis.

## Bayesian A/B testing

In Bayesian methods, We are mainly trying to solve the problem of Explore-exploit dilemma. We want to collect data (ex. Click through rate) between 2 websites to determine which one is better, but how do we know how much data we need to collect to determine the website with the highest CTR? Since there will be a better and a worse website, while collecting the data on the worse website, we are losing resources on directing customers to the worse website. Therefore, there are Two opposing force:

- Collect data (exploration, to make more accurate prediction)
- Select choice with highest win rate (exploitation)

Here, I implemented four methods that could solve the dilemma:

- Epsilon-greedy
- Optimistic Initial Values
- Upper Confidence Bound (UCB)
- Thompson Sampling (Bayesian Bandit)

There is also a simulation program that apply the UCB method to simulate the A/B testing for clicking two versions of ads. Please follow the steps below to start the simulation:
- download the files in the folder "ad_click_simulation"
- Run "python server.py"
- When server.py started, run "python client.py" on a separate terminal
- Once the client script started, on the server terminal, you would see that the server is getting ad viewed and ad clicked. When an ad is clicked, it would print some info about that ad (the ad version name, its view times and its click times).
