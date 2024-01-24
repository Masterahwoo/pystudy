# # 2.3
# name = "jingyan"
# msg= f"Hello {name.title()}, welcome"
# print(msg)

# # 2.4
# name = "xu JIngyan"
# print(name.lower())
# print(name.upper())
# print(name.title()

# bikes=['trek','redline','specialized']
# msg=f"my first bike is {bikes[0].title()}"
# print(msg)

# message = input ('input something and i will send it back to you')
# print(message) 

# unconfirmed_users=['alice','brian','cadance']
# confirmed_users = []

# while(unconfirmed_users):
#     current_user=unconfirmed_users.pop()
#     print(f"Verifiing User: {current_user.title()}")

#     confirmed_users.append(current_user)

# print("\nThe following users have been verified:")
# for user in confirmed_users:
#     print(user.title())


# -- coding utf-8 --
# Python 3
import base64
import http.client

# 客户 ID
# 需要设置环境变量 AGORA_CUSTOMER_KEY
customer_key = "82cc701512f547cd8ec0f9a21dfd60a8"
# 客户密钥
# 需要设置环境变量 AGORA_CUSTOMER_SECRET
customer_secret = "8778f20d63b24b6895a45181cd3d2463"

# 拼接客户 ID 和客户密钥
credentials = customer_key + ":" + customer_secret
# 使用 base64 进行编码
base64_credentials = base64.b64encode(credentials.encode("utf8"))
credential = base64_credentials.decode("utf8")
# 创建 authorization header
basic_auth_header = 'basic ' + credential

print(basic_auth_header)