import os
from uuid import uuid4


def unique_image_upload_path(instance, filename, subfolder='uploads'):
    """
    Generate unique filename for image uploads.

    Args:
        instance: Model instance
        filename: Original filename
        subfolder: Subfolder path (e.g., 'posts/covers', 'events/images')

    Returns:
        str: Unique file path in format: {subfolder}/{uuid}.{extension}

    Example:
        uploads/a3c4e5f6-1234-5678-9abc-def012345678.jpg
    """
    ext = os.path.splitext(filename)[1]
    unique_filename = f"{uuid4()}{ext}"
    return os.path.join(subfolder, unique_filename)


def post_cover_image_upload_path(instance, filename):
    """
    Generate unique filename for post cover images.
    Format: posts/covers/{uuid}.{extension}
    """
    return unique_image_upload_path(instance, filename, 'posts/covers')


def event_image_upload_path(instance, filename):
    """
    Generate unique filename for event images.
    Format: events/covers/{uuid}.{extension}
    """
    return unique_image_upload_path(instance, filename, 'events/covers')
