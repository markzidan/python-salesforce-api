API_VERSION = '44.0'

BULK_STATE_OPEN = 'Open'
BULK_STATE_UPLOAD_COMPLETE = 'UploadComplete'
BULK_STATE_ABORTED = 'Aborted'
BULK_STATE_JOB_COMPLETE = 'JobComplete'
BULK_STATE_FAILED = 'Failed'
BULK_STATES_DONE = [BULK_STATE_JOB_COMPLETE, BULK_STATE_ABORTED, BULK_STATE_FAILED]
BULK_STATES_FAIL = [BULK_STATE_ABORTED, BULK_STATE_FAILED]

TEST_LEVEL_NO_TEST_RUN = 'NotestRun'
TEST_LEVEL_RUN_SPECIFIED_TESTS = 'RunSpecifiedTests'
TEST_LEVEL_RUN_LOCAL_TESTS = 'RunLocalTests'
TEST_LEVEL_RUN_ALL_TESTS_IN_ORG = 'RunAllTestsInOrg'
TEST_LEVELS = [
    TEST_LEVEL_NO_TEST_RUN,
    TEST_LEVEL_RUN_SPECIFIED_TESTS,
    TEST_LEVEL_RUN_LOCAL_TESTS,
    TEST_LEVEL_RUN_ALL_TESTS_IN_ORG
]

STATUS_SUCCEEDED = 'Succeeded'
STATUS_FAILED = 'Failed'
STATUS_QUEUED = 'Queued'
STATUS_PENDING = 'Pending'
STATUS_INPROGRESS = 'InProgress'
STATUSES_PENDING = [
    STATUS_QUEUED,
    STATUS_PENDING,
    STATUS_INPROGRESS
]
STATUSES_DONE = [
    STATUS_SUCCEEDED,
    STATUS_FAILED
]