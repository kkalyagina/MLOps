import kk_lab

def main():
    print (kk_lab.get_df("AAPL", "7d"))
    print(kk_lab.plot_7d(kk_lab.get_df("AAPL", "7d"), './apple.png'))