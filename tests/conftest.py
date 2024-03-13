import logging

import pytest  # pyright: ignore [reportMissingImports]
from loguru import logger


@pytest.fixture()
def caplog(_caplog):
	"""Wrapper over caplog fixture to fix loguru logs.

	Parameters
	----------
	_caplog: Pytest fixture

	Yields
	------
	_caplog: Pytest fixture
	"""

	class PropogateHandler(logging.Handler):
		def emit(self, record):
			logging.getLogger(record.name).handle(record)

	logger.add(PropogateHandler(), format="{message}")
	handler_id = logger.add(PropogateHandler(), format="{message}")
	yield _caplog
	logger.remove(handler_id)
