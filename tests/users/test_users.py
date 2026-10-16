
class TestUsers:

    def test_get_user_info_without_token(self, api_manager):
        response = api_manager.user_api.get_user_info(expected_status=401)

        assert response.json()["error"]["code"] == "TOKEN_MISSING"

    def test_get_user_info(self, api_manager, authenticated_user):
        response = api_manager.user_api.get_user_info()

        user = response.json()

        assert user["email"] == authenticated_user["email"]
        assert user["id"] == authenticated_user["id"]