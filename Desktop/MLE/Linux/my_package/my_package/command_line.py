import my_package

def main():
    print (my_package.get_df("AAPL", "7d"))
    print(my_package.plot_7d(my_package.get_df("AAPL", "7d")))