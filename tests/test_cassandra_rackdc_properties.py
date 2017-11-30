import filecmp
import pytest

import cassandra_jinja2.cassandra_rackdc_properties

###################################################################################################################
# SETUP & TEARDOWN FUNCTIONS - that run before and after each test_ method.
###################################################################################################################


def setup_function():
    print()


def teardown_function():
    print()


###################################################################################################################
# FIXTURES
###################################################################################################################

@pytest.fixture
def cassandra_version():
    return '3.0.15'


###################################################################################################################
# TESTS
###################################################################################################################


def test_logback_xml(cassandra_version):
    config_file = './tests/files/apache-cassandra-{}/conf/cassandra-rackdc.properties'.format(cassandra_version)
    template_file = '/tmp/templates/apache-cassandra-{}/conf/cassandra-rackdc.properties.jinja'.format(cassandra_version)
    rendered_file = '/tmp/templates/apache-cassandra-{}/conf/cassandra-rackdc.properties'.format(cassandra_version)

    config = cassandra_jinja2.cassandra_rackdc_properties.CassandraRackDcProperties(cassandra_version)
    config.read(config_file)
    config.generate_template()
    config.write(template_file)
    # Test rendering the template_file with an empty context, ie. render the template file with the default values.
    # This should render the template_file as the original vanilla config file.
    config.render(template_file, rendered_file, context={'cassandra_rackdc_properties': {}})
    assert filecmp.cmp(rendered_file, config_file)
