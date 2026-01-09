from fastapi import HTTPException

def success(data=None,message='No message'):
    return {
        "success": True,
        "message": message,
        "data": data,
    }
    
def error(status_code=401,data=None,message='No message'):
    raise HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "message": message,
            "data": data,
        }
    )








