import os
import unittest


class TestWorkflow(unittest.TestCase):

  def test_log_file_creation(self):
    """Verify that the workflow script executes and generates a log file."""
    # Remove log file if it already exists from a previous run
    log_filename = 'workflow_log.txt'
    if os.path.exists(log_filename):
      os.remove(log_filename)

    # Execute the workflow script
    exit_code = os.system('python3 check_workflow.py')

    # Assertions
    self.assertEqual(exit_code, 0, 'The workflow script failed to execute.')
    self.assertTrue(
        os.path.exists(log_filename), 'The workflow log file was not created.'
    )

    # Clean up the created log file after a successful test
    if os.path.exists(log_filename):
      os.remove(log_filename)


if __name__ == '__main__':
  unittest.main()
