import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="Interação com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"ola": "mundo"}
    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="Interação com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    my_docs = [{"elem1": "aqui1"}, {"elem2": "aqui2"}, {"elem3": "aqui3"}]
    orders_repository.insert_list_of_documents(my_docs)


@pytest.mark.skip(reason="Interação com o banco")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many(doc_filter)
    print()
    print(response)
    for doc in response:
        print(doc)
        print(doc["items"])
        print()


@pytest.mark.skip(reason="Interação com o banco")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_one(doc_filter)
    print()
    print(response)


@pytest.mark.skip(reason="Interação com o banco")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()


@pytest.mark.skip(reason="Interação com o banco")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()
    print()
    for doc in response:
        print(doc)
        print()


@pytest.mark.skip(reason="Interação com o banco")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    # Semelhante a uma busca AND em SQL
    doc_filter = {
        "cupom": True,
        "items.refrigerante": {"$exists": True}}
    response = orders_repository.select_many(doc_filter)
    print()
    for doc in response:
        print(doc)
        print()


@pytest.mark.skip(reason="Interação com o banco")
def test_select_many_with_multiple_or_filter():
    orders_repository = OrdersRepository(conn)
    # Semelhante a uma busca OR em SQL
    doc_filter = {
        "$or": [
            {"address": {"$exists": True}},
            {"items.doce.tipo": "chocolate"}
        ]
    }
    response = orders_repository.select_many(doc_filter)
    print()
    print()
    for doc in response:
        print(doc)
        print()


@pytest.mark.skip(reason="Interação com o banco")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    object_id = "68069c2c7a1e1448207b0b85"
    response = orders_repository.select_by_object_id(object_id)
    print()
    print(response)


@pytest.mark.skip(reason="Interação com o banco")
def test_edit_registry():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry()


@pytest.mark.skip(reason="Interação com o banco")
def test_edit_many_registries():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_many_registries()


@pytest.mark.skip(reason="Interação com o banco")
def test_edit_registry_with_increment():
    orders_repository = OrdersRepository(conn)
    orders_repository.edit_registry_with_increment()
