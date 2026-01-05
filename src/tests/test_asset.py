

def test_load_asset(mocker):
    from src.logic.asset import AssetManager
    fake_surface = mocker.Mock()
    # simulate convert_alpha method
    fake_surface.convert_alpha.return_value = fake_surface
    load_mock = mocker.patch(
        "src.logic.asset.pygame.image.load",
        return_value=fake_surface
    )
    asset_manager = AssetManager()
    a1 = asset_manager.load_image("pieces/black_pawn.png")
    a2 = asset_manager.load_image("pieces/black_pawn.png")
    assert a1 is fake_surface
    assert a2 is fake_surface
    load_mock.assert_called_once()
