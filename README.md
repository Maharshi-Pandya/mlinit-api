# mLinit API

🚀 this repository consists of the mLinit API (Application Programming Interface) for analyzing any CSV dataset(s).

there will be 4 endpoints as of now:

- `/info?apiKey=<your_api_key_here>`

    for dataset information such as **column names**, **null values count**, and more


- `/des?apiKey=<your_api_key_here>`

    for dataset summary statistics (**mean**, **standard deviation**, etc...)


- `/dup?apiKey=<your_api_key_here>`

    for getting the number of duplicate rows in the dataset
    

- `/corr?apiKey=<your_api_key_here>`

    for analyzing linear correlation between dataset columns


- `/viz?apiKey=<your_api_key_here>`

    for data visualization operations