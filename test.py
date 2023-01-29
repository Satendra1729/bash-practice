import types
import requests; 


def test_result_mapper(result) : 
    return "Pass" if result else "Fail"; 

def test_name_parser(testName) : 
    return " ".join([e[0].upper()+e[1:]
                for e in  
                testName.split("_")])

def user_name_is_george(): 
    URL = "https://reqres.in/api/users"; 

    jRes = requests.get(URL).json()["data"]

    user1Name = [o for o in jRes if o["id"]==1][0]["first_name"]

    return user1Name=="Georg"


if __name__=="__main__": 
    testlst = [{
        "test_name": user_name_is_george
    }]
    for o in testlst : 
        o["result"] = test_result_mapper(user_name_is_george())
        
    isinstance(user_name_is_george, types.FunctionType); 
    
    headers = ",".join(testlst[0].keys())
        
    testresults  = [ ",".join([   test_name_parser(ele.__name__)
                                         if isinstance(ele, types.FunctionType)
                                         else str(ele)
                                         for ele in o.values()]) for o in  testlst]
    
    testresults.insert(0,headers)

    
    print("\n".join(testresults))