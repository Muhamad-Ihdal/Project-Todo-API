from fastapi import HTTPException

def success(data=None,massage='No massage'):
    return {
        "success": True,
        "massage": massage,
        "data": data,
    }
    
def error(status_code=401,data=None,massage='No massage'):
    return HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "massage": massage,
            "data": data,
        }
    )

def not_found_error(status_code=404,data=None,massage='data tidak di temukan'):
    return HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "massage": massage,
            "data": data,
        }
    )
def forbidden_error(status_code=403,data=None,massage='Forbidden'):
    return HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "massage": massage,
            "data": data,
        }
    )







