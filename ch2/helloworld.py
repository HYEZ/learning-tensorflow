import tensorflow as tf
print(tf.__version__)

h = tf.constant("Hello")
w = tf.constant("World!")
hw = h + w # 나중에 실행될 합 연산을 연산 그래프에 추가함
print(hw)

with tf.Session() as sess:
	ans = sess.run(hw)

print(ans)


# 텐서플로우는 어떤 연산을 할 지 정해두고, 외부 메커니즘을 통해서 그 연산을 실행시킨다