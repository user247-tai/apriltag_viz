import launch
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():
    composable_node = ComposableNode(
        package='apriltag_viz',
        plugin='AprilVizNode',   # or "apriltag_viz::AprilVizNode" if it’s in a namespace
        name='viz',
        remappings=[
            ('/apriltag/image', '/detect/image')
        ],
    )

    container = ComposableNodeContainer(
        name='viz_container',
        namespace='apriltag',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=[composable_node],
        output='screen',
    )

    return launch.LaunchDescription([container])