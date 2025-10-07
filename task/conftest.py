
import logging

logging.basicConfig(
    filename="pytest_results.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


def pytest_configure(config):
    config.addinivalue_line("markers", "tag(name): mark test with a custom tag")
    logger.info("PyTest session started.")


def pytest_collection_modify_items(config, items):
    selected_tag = config.getoption("--tag")
    if selected_tag:
        logger.info(f"Filtering tests with tag: {selected_tag}")
        selected = []
        deselected = []
        for item in items:
            tags = [mark.args[0] for mark in item.iter_markers(name="tag")]
            if selected_tag in tags:
                selected.append(item)
            else:
                deselected.append(item)
        items[:] = selected
        config.hook.pytest_deselected(items=deselected)


def pytest_runtest_log_report(report):
    if report.when == "call":
        if report.failed:
            logger.error(f"❌ {report.nodeid} FAILED")
        elif report.skipped:
            logger.warning(f"⚠️ {report.nodeid} SKIPPED")
        else:
            logger.info(f"✅ {report.nodeid} PASSED")

def pytest_addoption(parser):
    parser.addoption("--tag",action="store",default=None,help="Run tests with a specific custom tag")

