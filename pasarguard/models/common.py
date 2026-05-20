from __future__ import annotations

from ._base import Any, Dict, List, Optional, PasarguardModel, Union

class BaseNotificationEnable(PasarguardModel):
    create: Optional[bool] = True
    modify: Optional[bool] = True
    delete: Optional[bool] = True

class Conflict(PasarguardModel):
    detail: Optional[str] = 'Entity already exists'

class Forbidden(PasarguardModel):
    detail: Optional[str] = 'You are not allowed to ...'

class HTTPException(PasarguardModel):
    detail: str = ...

class HTTPRequest(PasarguardModel):
    version: Optional[str] = '1.1'
    headers: Optional[Dict[str, List[str]]] = None
    method: Optional[str] = 'GET'

class HTTPResponse(PasarguardModel):
    version: Optional[str] = '1.1'
    headers: Optional[Dict[str, List[str]]] = None
    status: Optional[str] = '200'
    reason: Optional[str] = 'OK'

class HTTPValidationError(PasarguardModel):
    detail: Optional[List[ValidationError]] = None

class NotFound(PasarguardModel):
    detail: Optional[str] = 'Entity {} not found'

class Unauthorized(PasarguardModel):
    detail: Optional[str] = 'Not authenticated'

class ValidationError(PasarguardModel):
    loc: List[Union[str, int]] = ...
    msg: str = ...
    type: str = ...
    input: Any = None
    ctx: Optional[Dict[str, Any]] = None

__all__ = (
    'BaseNotificationEnable',
    'Conflict',
    'Forbidden',
    'HTTPException',
    'HTTPRequest',
    'HTTPResponse',
    'HTTPValidationError',
    'NotFound',
    'Unauthorized',
    'ValidationError',
)
