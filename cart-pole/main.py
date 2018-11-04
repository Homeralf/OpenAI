import gym
import time


N_STEPS = 1000
N_EPISODES = 30

x_discrete = [-0.8, 0.8]
x_dot_discrete = [-0.5, 0.5]
theta_discrete = [-6, -1, 0, 1, 6]
theta_dot_discrete = [-15, 15]
discrete_observation_state_buckets = [x_discrete, x_dot_discrete, theta_discrete, theta_dot_discrete]


class DiscreteObservationState:
    """
    This class generates the buckets needed to apply Q-learning
    The space is divided as follows:
        - x: position [-4.8, 4.8]
        - x': velocity [-inf, inf]
        - theta: angle [-4.19, 4.19]
        - theta': angle [-inf, inf]
    """

    def __init__(self, discrete_observation_state_buckets):
        self.discrete_observation_buckets = discrete_observation_state_buckets
        self._discrete_observation_space = {}

    def _build_discrete_observation_state(self, discrete_observation_space_buckets):
        for i, dimension in enumerate(discrete_observation_state_buckets):
            self._discrete_observation_space[i] = {}



    def get_action(self, continious_observation):
        pass

    def _discretize_x(self):
        pass

def main():
    env = gym.make('CartPole-v0')
    max_n_steps = 0
    good_guesses = 1
    for i in range(1, N_EPISODES):
        # print(i)
        print("Observation Space {}".format(env.observation_space.high))
        done = False
        env.reset()
        action = 1
        while not done:
            observation, reward, done, info = env.step(action)
            env.render()
            time.sleep(0.01)
    env.close()


if __name__ == "__main__":
    main()