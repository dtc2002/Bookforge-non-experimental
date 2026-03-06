from unittest import TestCase
from unittest.mock import patch
from pathlib import Path
import json

from literary_ai import cli
from literary_ai.sqlite_store import create_character

class TestLiteraryAICLI(TestCase):
    def setUp(self):
        self.project_dir = Path("test_project")
        self.project_dir.mkdir(exist_ok=True)
        
    def tearDown(self):
        self.project_dir.rmdir()

    @patch("literary_ai.cli.typer.echo")
    def test_init_command(self, mock_echo):
        cli.init(name="test_project")
        
        # Check if directories were created
        self.assertTrue((self.project_dir / "stories").exists())
        self.assertTrue((self.project_dir / "characters").exists())
        self.assertTrue((self.project_dir / "canon").exists())
        
        # Check if config file was created
        config_path = self.project_dir / "config.json"
        self.assertTrue(config_path.exists())
        
        # Check config content
        with config_path.open("r") as f:
            config = json.load(f)
            self.assertEqual(config["name"], "test_project")
            self.assertEqual(config["author"], "Your Name")

    def test_pipeline_command(self):
        # Test pipeline command output
        with patch("literary_ai.cli.typer.echo") as mock_echo:
            cli.pipeline()
            mock_echo.assert_called_with("Running literary AI pipeline")