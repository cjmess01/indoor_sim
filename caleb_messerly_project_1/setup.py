from setuptools import find_packages, setup

package_name = 'caleb_messerly_project_1'

data_files = []
data_files.append(('share/ament_index/resource_index/packages', ['resource/' + package_name]))
data_files.append(('share/' + package_name + '/launch', ['launch/caleb_messerly_project_1_launch.py']))

data_files.append(('share/' + package_name + '/worlds', [
    'worlds/paty_floor.wbt',
]))
data_files.append(('share/' + package_name, ['package.xml']))
data_files.append(('share/' + package_name + '/resource', [
    'resource/turtlebot_webots.urdf',
    'resource/ros2control.yml',
]))

setup(
    name='caleb_messerly_project_1',
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools', 'launch'],
    zip_safe=True,
    maintainer='Caleb Messerly-UA',
    maintainer_email='cjmesserly@crimson.ua.edu',
    description='A world file for a portion of Paty Halls 2nd floor',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],
        'console_scripts': ['caleb_messerly_project_1 = caleb_messerly_project_1.caleb_messerly_project_1:main']
    },

)
