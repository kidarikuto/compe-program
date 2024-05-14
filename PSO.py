import random

# 目的関数
def objective_function(x):
    return (x - 1) ** 2

# PSOのパラメータ
num_particles = 3
positions = [-3, 2, 6]
velocities = [0, 0, 0]
personal_best_positions = positions[:]
personal_best_scores = [objective_function(x) for x in positions]
global_best_position = positions[personal_best_scores.index(min(personal_best_scores))]
global_best_score = min(personal_best_scores)

# 学習係数
c1 = c2 = 1

# PSOの実行
num_iterations = 5
for iteration in range(num_iterations):
    print(f"Iteration {iteration + 1}")
    for i in range(num_particles):
        # 速度の更新
        r1, r2 = random.random(), random.random()
        # velocities[i] = velocities[i] + c1 * r1 * (personal_best_positions[i] - positions[i]) + c2 * r2 * (global_best_position - positions[i])
        velocities[i] = velocities[i] + c1 * (personal_best_positions[i] - positions[i]) + c2  * (global_best_position - positions[i])
        # 位置の更新
        positions[i] += velocities[i]
        
        # 評価
        current_score = objective_function(positions[i])
        
        # 個人のベスト更新
        if current_score < personal_best_scores[i]:
            personal_best_positions[i] = positions[i]
            personal_best_scores[i] = current_score
        
        # グローバルベストの更新
        if current_score < global_best_score:
            global_best_position = positions[i]
            global_best_score = current_score
        
        print(f"  Particle {i + 1}: Position = {positions[i]:.4f}, Velocity = {velocities[i]:.4f}, Score = {current_score:.4f}")

    print(f"Global Best Position: {global_best_position:.4f}, Global Best Score: {global_best_score:.4f}")
    print("-" * 50)