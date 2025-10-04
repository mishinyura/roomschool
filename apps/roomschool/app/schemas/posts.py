"""
Schemas for Post and Author entities.

This module contains Pydantic models that represent the data structures
used for validation and serialization of post-related data. These schemas
are typically used in FastAPI routes as request/response models.
"""

from pydantic import BaseModel


class PostAuthor(BaseModel):
    """
    Schema representing an author of a post.

    Attributes:
        name: Display name of the author.
        post: Job title or role of the author (optional).
        image_url: URL of the author's avatar or photo (optional).
    """

    name: str
    post: str | None
    image_url: str | None

    model_config = {"from_attributes": True}


class PostBase(BaseModel):
    """
    Base schema for a blog/news post.

    Attributes:
        id: Unique identifier of the post.
        slug: Slugified identifier for use in URLs.
        title: Title of the post.
        description: Short description or summary of the post.
        author: Nested PostAuthor schema with author details.
        is_archived: Boolean flag indicating whether the post is archived.
    """

    id: int
    slug: str
    title: str
    description: str
    author: PostAuthor
    is_archived: bool

    model_config = {"from_attributes": True}


class PostOutClient(BaseModel):
    """
    Public schema for returning post data to clients.

    This schema contains only the fields visible to end users (no ID, slug, or archive status).

    Attributes:
        title: Title of the post.
        description: Short description of the post.
        author: Nested PostAuthor schema with author details.
    """

    title: str
    description: str
    author: PostAuthor

    model_config = {"from_attributes": True}
