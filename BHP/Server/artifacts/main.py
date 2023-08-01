import os
import pickle
file_path = 'C:\Users\Asus\House Price Prediction\BHP\Server\artifacts/banglore_home_prices_model.pickle'

if os.path.getsize(file_path) > 0:
    with open(file_path, 'rb') as my_file:
        unpickler = pickle.Unpickler(my_file)
        employee_data = unpickler.load()
        print(employee_data)
else:
    print('The file is empty')
