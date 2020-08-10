class A(object):
    bar = 1
    def foo(self):
        print('foo')

    @staticmethod
    def static_foo():
        print('static foo')
        print(A.bar)

    @classmethod
    def class_foo(cls):
        print('class foo')
        print(cls.bar)
        cls.bar += 1
        cls().foo()

# A.static_foo()
# A.class_foo()

a = A()
a.class_foo()

b = A()
b.class_foo()