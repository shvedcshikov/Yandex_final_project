#Шведчиков Алексей, 21а когорта - Финальный проект. Инженер по тестированию плюс

import create_order
def test_positive_assert():
    assert create_order.order_response.status_code==200
