import pytest

from television import Television

def main():
    def test_init():
        TV = Television()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"
    

    def test_power():
        TV = Television()
        out = "Power = False, Channel = 0, Volume = 0"
        assert str(TV) == out
        TV.power()
        assert str(TV) == "Power = True, Channel = 0, Volume = 0"
    

        
    def test_mute():
        TV = Television()
        out = "Power = True, Channel = 0, Volume = 0"
        TV.power()
        TV.volume_up()
        TV.mute()
        assert str(TV) == out
        TV = Television()
        TV.power()
        assert str(TV) == "Power = True, Channel = 0, Volume = 0"
        TV = Television()
        TV.mute()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"
        TV = Television()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"


    def test_channel_up():
        TV = Television()
        TV.channel_up()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"
        TV = Television()
        TV.power()
        TV.channel_up()
        assert str(TV) == "Power = True, Channel = 1, Volume = 0"
        TV = Television()
        TV.power()
        TV.channel_up()
        TV.channel_up()
        TV.channel_up()
        TV.channel_up()
        assert str(TV) == "Power = True, Channel = 0, Volume = 0"

    def test_channel_down():
        TV = Television()
        TV.channel_down()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"
        TV.power()
        TV.channel_down()
        assert str(TV) == "Power = True, Channel = 3, Volume = 0"


    def test_volume_up():
        TV = Television()
        TV.volume_up()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"
        TV.power()
        TV.volume_up()
        assert str(TV) == "Power = True, Channel = 0, Volume = 1"
        TV.mute()
        TV.volume_up()
        assert str(TV) == "Power = True, Channel = 0, Volume = 2"

    
    def test_volume_down():
        TV = Television()
        TV.volume_down()
        assert str(TV) == "Power = False, Channel = 0, Volume = 0"
        TV.power()
        TV.volume_down()
        assert str(TV) == "Power = True, Channel = 0, Volume = 0"
        TV = Television()
        TV.power()
        TV.mute()
        TV.volume_down()
        assert str(TV) == "Power = True, Channel = 0, Volume = 0"
        TV = Television()
        TV.power()
        TV.volume_down()
        TV.volume_down()
        assert str(TV) == "Power = True, Channel = 0, Volume = 0"
        





    test_channel_up()
    test_init()
    test_power()
    test_mute()
    test_channel_down()
    test_volume_up()
    test_volume_down()


if __name__ == "__main__":
    main()
