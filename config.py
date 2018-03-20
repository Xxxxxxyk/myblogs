#激活跨站点请求伪造保护,激活可以保证项目安全
CSRF_ENABLED = True
#当CSRF激活时,创建一个加密令牌,用于验证表单
SECRET_KEY = 'you-will-newver-guess'

OPENID_PROVIDERS = [
	{'name' : 'Google','url' : 'https://www.google.com/accounts/o8/id'},
	{ 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]