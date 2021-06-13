# FastAPI + Ariadne によるCRUD機能

## 環境
- python3.9
- FastAPI
- MySQL5.7

## 構築

### docker-composeによるビルド
~~~
$ docker-compose up -d --build
~~~

### テーブルの作成

1. api側のコンテナにアクセスする。
2. アクセス後以下のコマンドを実行する。
~~~
$ python 
>>> from domains import todo
>>> from db import engine
>>> todo.Base.metadata.create_all(bind=engine)
~~~

## アクセス
http://localhost:8000


## Query

### 全データ取得

~~~ 
query{
  listTodos {
    success,
    errors,
    todos{
      id
      title
      content
      created_at
    }
  }
}
~~~

### 検索
~~~
query{
  getTodo(id: "4") {
    success,
    errors,
    todo{
      id
      title
      content
      created_at
    }
  }
}
~~~

### 作成
~~~
mutation {
  createTodo(
    title: "sampleA",
  	content: "Sample content") {
    success,
    errors,
    todo{
      id
      title
      content
      created_at
    }
  }
}
~~~

### 更新 
~~~
mutation {
  updateTodo(id: "2", title: "update sampleA", content: "this is UpdateGraphqlAPI") {
    success,
    errors,
    todo{
      id
      title
      content
      created_at
    }
  }
}
~~~

### 削除
~~~
mutation {
  deleteTodo(id: "3") {
    success,
    errors
    todo{
      id
      title
      content
      created_at
    }
  }
}
~~~