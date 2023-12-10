import requests


# response = requests.post(
#     'http://127.0.0.1:5000/ads/add',
#     json={
#         'title': 'Nik',
#         'description': 'jkl;kl;k',
#         'author': 'Sasha'
#         }
# )
# print(response.text)


response = requests.patch(
    "http://127.0.0.1:5000/ads/edit/1",
    json={
        "title": "Nik_2",
    },
)
print(response.text)

#
# response = requests.delete(
#     'http://127.0.0.1:5000/ads/delete/1'
# )
# print(response.text)
