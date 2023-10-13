# TicTacToeBackends SDK


## Overview

Game Engine API for Tic Tac Toe: Game Engine API for Tic Tac Toe

### Available Operations

* [get_](#get_) - Root endpoint.
* [get_version](#get_version) - Root endpoint.
* [put_games](#put_games) - Games endpoint. Creates the next game state from the previous game state.

## get_

<br/>Returns the package name and version.<br/><br/>

### Example Usage

```python
import tic_tac_toe_backends


s = tic_tac_toe_backends.TicTacToeBackends()


res = s.tic_tac_toe_backends.get_()

if res.body is not None:
    # handle response
    pass
```


### Response

**[operations.GetResponse](../../models/operations/getresponse.md)**


## get_version

<br/>Returns the package name and version.<br/><br/>

### Example Usage

```python
import tic_tac_toe_backends


s = tic_tac_toe_backends.TicTacToeBackends()


res = s.tic_tac_toe_backends.get_version()

if res.body is not None:
    # handle response
    pass
```


### Response

**[operations.GetVersionResponse](../../models/operations/getversionresponse.md)**


## put_games

<br/>Accepts a GameState and Move.<br/><br/>Returns a Move including the before and after GameStates.<br/>

### Example Usage

```python
import tic_tac_toe_backends
from tic_tac_toe_backends.models import shared

s = tic_tac_toe_backends.TicTacToeBackends()

req = 'GjnqQzHiDc'.encode()

res = s.tic_tac_toe_backends.put_games(req)

if res.body is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models//.md)                 | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PutGamesResponse](../../models/operations/putgamesresponse.md)**

