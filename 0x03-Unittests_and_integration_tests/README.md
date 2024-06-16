0x03. Unittests and Integration Tests

Learning Objectives:
	- The difference between unit and integration tests.
	- Common testing patterns such as mocking, parametrizations and fixtures

Key Concepts:
	- unittest — Unit testing framework
		test fixture, test case, test suite, test runner
	- unittest.mock — mock object library
	- How to mock a readonly property with mock?
	- parameterized, nose.tools, @parameterized and @parameterized.expand decorators
	- Parameterized testing for nose, parameterized testing for py.test, parameterized testing for unittest
	- Memoization
	- how to use Mock, MagicMock and patch()
	- The Mock Class

Functions and Code snippets:
	unittest.TestCase class
	self.assertEqual()
	self.assertTrue()
	self.assertFalse()
	self.assertEqual()
	self.assertRaises()
	split()
	unittest.main()
	setUp() and tearDown()
	-v option in unittest.main()

	CLI:
	-> python -m unittest test_module1 test_module2
	-> python -m unittest test_module.TestClass
	-> python -m unittest test_module.TestClass.test_method

	-> python -m unittest tests/test_something.py
	-> python -m unittest -v test_module
	-> python -m unittest
	-> python -m unittest -h

	TestLoader.discover()
	python -m unittest discover -s project_directory -p "*_test.py"
	python -m unittest discover project_directory "*_test.py"

	skip() TestCase.skipTest()
	setUpClass() tearDownClass() run(result=None) skipTest(reason) subTest(msg=None, **params) debug()
	
	Method			Checks that		New in

	assertEqual(a, b)	a == b

	assertNotEqual(a, b)	a != b

	assertTrue(x)		bool(x) is True

	assertFalse(x)		bool(x) is False

	assertIs(a, b)		a is b			3.1

	assertIsNot(a, b)	a is not b		3.1

	assertIsNone(x)		x is None		3.1

	assertIsNotNone(x)	x is not None		3.1

	assertIn(a, b)		a in b			3.1

	assertNotIn(a, b)	a not in b		3.1

	assertIsInstance(a, b)	isinstance(a, b)	3.2

	assertNotIsInstance(a, b) not isinstance(a, b)	3.2

	unittest.mock MagicMock() patch()
