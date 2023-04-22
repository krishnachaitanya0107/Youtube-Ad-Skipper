import pytest
from youtube_ad_skipper import YoutubeAdSkipper

class TestYoutubeAdSkipper:
    @pytest.fixture
    def ad_skipper(self):
        return YoutubeAdSkipper()

    def test_load_templates(self, ad_skipper):
        ad_skipper.load_templates()
        assert len(ad_skipper.templates) == 4

    def test_open_video(self, ad_skipper, monkeypatch):
        def mock_open_new(url):
            assert url == "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
        monkeypatch.setattr('webbrowser.open_new', mock_open_new)
        ad_skipper.video_url_entry.delete(0, 'end')
        ad_skipper.video_url_entry.insert(0, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        ad_skipper.open_video()

    def test_start_and_stop(self, ad_skipper):
        ad_skipper.start()
        assert ad_skipper.task is not None
        ad_skipper.stop()
        assert ad_skipper.task is None
