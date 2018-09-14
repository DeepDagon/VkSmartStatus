import vk_api

vk_session = vk_api.VkApi(token= 'dd38b1ee28a878e995d013ddea790414f810f1573e2d1f99b710679940e71425354d49d7ff953ebd43eba')
vk = vk_session.get_api()
on = vk.wall.post(message='124')
