

def test_load_asset(mocker):
    from src.logic.asset import AssetManager
    fake_surface = mocker.Mock()
    load_mock = mocker.patch("pygame.image.load", return_value=fake_surface)
    asset_manager = AssetManager()
    a1 = asset_manager.load_image("pieces/black_pawn.png")
    a2 = asset_manager.load_image("pieces/black_pawn.png")
    assert a1 is a2
    load_mock.assert_called_once()
