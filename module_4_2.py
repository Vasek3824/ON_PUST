def test_function():
    def inner_function():
        print(f'Я в области видимости функции {test_function}')

    inner_function()
test_function()

#inner_function() - вызов этой функции в глобальном пространстве вызовит ошибку, т.к. функция является локальным объектом для функции test_function 
