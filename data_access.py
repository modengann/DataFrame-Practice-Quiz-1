import pandas as pd

def get_age(df):
    pass

def get_third_name(df):
    pass

def get_carol_deets(df):
    pass

def get_salary_and_occupation(df):
    pass

def get_age_salary_of_first_two(df):
    pass

def get_occupation_bob_eve(df):
    pass


    

def main():
    df = pd.read_csv("data.csv", index_col = 0)
    print(df)
    
    print("****************")
    print(get_age(df))
    
    print("****************")
    print(get_third_name(df))
    
    print("****************")
    print(get_carol_deets(df))
    
    print("****************")
    print(get_salary_and_occupation(df))
    
    print("****************")
    print(get_age_salary_of_first_two(df))
    
    print("****************")
    print(get_occupation_bob_eve(df))
    
    
    
    
    

if __name__ == "__main__":
    main()