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


res = s.get_()

if res.body is not None:
    # handle response
    pass
```


### Response

**[operations.GetResponse](../../models/operations/getresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## get_version

<br/>Returns the package name and version.<br/><br/>

### Example Usage

```python
import tic_tac_toe_backends

s = tic_tac_toe_backends.TicTacToeBackends()


res = s.get_version()

if res.body is not None:
    # handle response
    pass
```


### Response

**[operations.GetVersionResponse](../../models/operations/getversionresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |

## put_games

<br/>Accepts a GameState and Move.<br/><br/>Returns a Move including the before and after GameStates.<br/>

### Example Usage

```python
import tic_tac_toe_backends

s = tic_tac_toe_backends.TicTacToeBackends()

req = '0x8BCDbF9B8f'.encode()

res = s.put_games(req)

if res.body is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                  | Type                                       | Required                                   | Description                                |
| ------------------------------------------ | ------------------------------------------ | ------------------------------------------ | ------------------------------------------ |
| `request`                                  | [bytes](../../models/.md)                  | :heavy_check_mark:                         | The request object to use for the request. |


### Response

**[operations.PutGamesResponse](../../models/operations/putgamesresponse.md)**
### Errors

| Error Object    | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.SDKError | 4x-5xx          | */*             |
