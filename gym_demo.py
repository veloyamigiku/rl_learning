import gym
import matplotlib.pyplot as plt
import pickle

def gen_state_label(state):
    state_text = f'cart position={state[0]:5.2f}, '
    state_text += f'cart velocity={state[1]:6.3f}\n'
    state_text += f'pole angle ={state[2]:5.2f}, '
    state_text += f'pole velocity={state[3]:6.3f}'
    return state_text

def save_render(
    output_path,
    render_data,
    state):

    plt.figure(figsize=(9, 7), facecolor='white')
    plt.suptitle('Cart Pole', fontsize=20)
    plt.imshow(render_data)
    plt.xticks(ticks=[])
    plt.yticks(ticks=[])
    state_text = gen_state_label(state)
    plt.title(state_text, loc='left')
    plt.savefig(output_path)
    plt.close()

env = gym.make('CartPole-v1', render_mode="rgb_array")

print(env.action_space)

print(env.observation_space)

print(env.reward_range)

for i in range(5):
    state, info = env.reset()
    #print('state:', state) # カートの位置、カートの速度、ポールの角度、ポールの角速度
    #print('info:', info)
    state_data = []
    render_data = [env.render()]
    for step in range(200):

        action = env.action_space.sample()

        next_state, reward, terminated, truncated, info = env.step(action)
        
        state_data.append((state, action, reward, terminated))
        render_data.append(env.render())

        print(
            'game=' + str(i + 1) +
            ', step=' + str(step + 1) +
            ', state(position)=' + str(state[0].round(3)) +
            ', action=' + str(action) +
            ', reward=' + str(reward) +
            ', terminated:' + str(terminated) +
            ', truncated:' + str(truncated)
        )

        if terminated:
            state_data.append((state, None, None, None))
            break

        state = next_state
    # save state_data, render_data(pickle)
