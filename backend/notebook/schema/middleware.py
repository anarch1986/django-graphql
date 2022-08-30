import os

class LoggerMiddleware(object):
    def resolve(self, next, root, info, **args):
        print('GraphQL endpoint called')
        return next(root, info, **args)
