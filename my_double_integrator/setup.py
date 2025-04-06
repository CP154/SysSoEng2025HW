from setuptools import find_packages, setup

package_name = 'my_double_integrator'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='varga',
    maintainer_email='vargabalint92@gmail.com',
    description='ROS 2 package for simulating and controlling a double integrator',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'double_integrator = my_double_integrator.double_integrator:main',
            'reference_position = my_double_integrator.reference_position:main',
            'controller = my_double_integrator.controller:main',
            'position_plotter = my_double_integrator.position_plotter:main',
        ],
    },
)
