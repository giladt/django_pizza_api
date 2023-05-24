# Pizza Order Management API

## Introduction

This django-admin api provides endpoints for managing client pizza orders.

## Install

- Clone this repo
- Run `cd django_pizza_api`
- Add `.env` file in the root folder containing the environment variables below.
- Run `docker-compose up --build -d`

This will install django and postgresql, create `superuser` with the credentials `pizza_admin` (password: `pizza`) and will seed the static tables: client, flavour, size, and status.

### Environment Variables

<code>
  SECRET_KEY=`your secret is safe`<br/>
  DEBUG=1<br/>
  DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]<br/>
  SQL_ENGINE=django.db.backends.postgresql<br/>
  SQL_DATABASE=pizza_order_management_db<br/>
  SQL_USER=pizza_admin<br/>
  SQL_EMAIL=admin@pizza.com<br/>
  SQL_PASSWORD=pizza<br/>
  SQL_HOST=db<br/>
  SQL_PORT=5432<br/>
  DATABASE=postgres<br/>
</code>

## Endpoints:

| Methods | Route                    | Description                 | Payload                                                      |
| :-----: | ------------------------ | --------------------------- | ------------------------------------------------------------ |
|   GET   | /api/client/             | List all clients            |                                                              |
|  POST   | /api/client/             | Create a new client         | { client_name: str, client_address: str, client_phone: str } |
|   GET   | /api/client/[int:id]     | Retrieve client by id       |                                                              |
|  PATCH  | /api/client/[int:id]     | Update client by id         | {client_name: str}                                           |
| DELETE  | /api/client/[int:id]     | Remove client by id         |                                                              |
|         |                          |                             |                                                              |
|   GET   | /api/flavour/            | List all flavours           |                                                              |
|   GET   | /api/flavour/[int:id]    | Retrieve flavour by id      |                                                              |
|         |                          |                             |                                                              |
|   GET   | /api/size/               | List all sizes              |                                                              |
|   GET   | /api/size/[int:id]       | Retrieve size by id         |                                                              |
|         |                          |                             |                                                              |
|   GET   | /api/status              | List all statuses           |                                                              |
|   GET   | /api/status/[int:id]     | Retrieve status by id       |                                                              |
|         |                          |                             |                                                              |
|   GET   | /api/item/               | List all items              |                                                              |
|  POST   | /api/item/               | Create a new item           | { flavour: int, size: int, amount: int, is_ready: bool }     |
|   GET   | /api/item/[int:id]       | Retrieve item by id         |                                                              |
|  PATCH  | /api/item/[int:id]       | Update (order) item by id   | {flavour: int}                                               |
| DELETE  | /api/item/[int:id]       | Remove item by id           |                                                              |
|         |                          |                             |                                                              |
|   GET   | /api/order/              | List all orders             |                                                              |
|  POST   | /api/order/              | Create a new order          | { client: int, status: int }                                 |
|   GET   | /api/order/[int:id]      | Retrieve order by id        |                                                              |
|  PATCH  | /api/order/[int:id]      | Update order by id          | { status: int }                                              |
| DELETE  | /api/order/[int:id]      | Remove (Client) order by id |                                                              |
|         |                          |                             |                                                              |
|   GET   | /api/order_item/         | List all order items        |                                                              |
|  POST   | /api/order_item/         | Create a new order item     | { order: int, item: int }                                    |
|   GET   | /api/order_item/[int:id] | Retrieve order item by id   |                                                              |
|  PATCH  | /api/order_item/[int:id] | Update order item by id     | { item: int }                                                |
| DELETE  | /api/order_item/[int:id] | Remove order item by id     |                                                              |

# Relations
