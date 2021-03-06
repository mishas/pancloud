# -*- coding: utf-8 -*-

"""Interact with the Application Framework Directory-Sync Service API.

To obtain rich information about users and devices for the purposes of
reporting and policy enforcement, cloud-based applications need access
to directory information. However, most directories are located
on-premise so they cannot be accessed by cloud-based applications.
The Directory Sync Service allows cloud-based applications to access
directory data by using an on-premise agent to collect it, and then
transferring the data to the cloud-based Directory-Sync Service.

Examples:
    Refer to the examples provided with this library.

"""

from __future__ import absolute_import
import logging

from .httpclient import HTTPClient


class DirectorySyncService(object):
    """An Application Framework Directory-Sync Service Instance."""

    def __init__(self, **kwargs):
        """

        Parameters:
            session (HTTPClient): :class:`~pancloud.httpclient.HTTPClient` object. Defaults to ``None``.
            url (str): URL to send API requests to. Later combined with ``port`` and :meth:`~request` ``path`` parameter.

        Args:
            **kwargs: Supported :class:`~pancloud.httpclient.HTTPClient` parameters.

        """
        self.kwargs = kwargs.copy()  # used for __repr__
        self.session = kwargs.pop('session', None)
        self._httpclient = self.session or HTTPClient(**kwargs)
        self.url = self._httpclient.url
        self._debug = logging.getLogger(__name__).debug

    def __repr__(self):
        for k in self.kwargs.get('headers', {}):
            if k.lower() == 'authorization':
                x = dict(self.kwargs['headers'].items())
                x[k] = '*' * 6  # starrify token
                return '{}({}, {})'.format(
                    self.__class__.__name__,
                    ', '.join('%s=%r' % (x, _) for x, _ in
                              self.kwargs.items() if x != 'headers'),
                    'headers=%r' % x
                )
        return '{}({})'.format(
            self.__class__.__name__,
            ', '.join(
                '%s=%r' % x for x in self.kwargs.items())
        )

    def attributes(self, **kwargs):  # pragma: no cover
        """Retrieve the attribute configuration object.

        Retrieves a mapping that identifies the custom directory
        attributes configured for the Directory SyncService instance,
        and the mapping of the custom attributes to standard directory
        attributes.

        Args:
            **kwargs: Supported :meth:`~pancloud.httpclient.HTTPClient.request` parameters.

        Returns:
            requests.Response: Requests Response() object.

        Examples:
            Refer to ``directory_attributes.py`` example.

        """
        path = "/directory-sync-service/v1/attributes"
        r = self._httpclient.request(
            method="GET",
            path=path,
            url=self.url,
            **kwargs
        )
        return r

    def count(self, object_class=None, params=None, **kwargs):  # pragma: no cover
        """Retrieve the attribute configuration object.

        Retrieve a count of all directory entries that belong to the
        identified objectClass. The count is limited to a single domain.

        Args:
            params (dict): Payload/request dictionary.
            object_class (str): Directory object class.
            **kwargs: Supported :meth:`~pancloud.httpclient.HTTPClient.request` parameters.

        Returns:
            requests.Response: Requests Response() object.

        Examples:
            Coming soon.

        """
        path = "/directory-sync-service/v1/{}/count".format(
            object_class
        )
        r = self._httpclient.request(
            method="GET",
            path=path,
            url=self.url,
            params=params,
            **kwargs
        )
        return r

    def domains(self, **kwargs):  # pragma: no cover
        """Retrieves a list of all domains available.

        Directory Sync Service can be configured to read directory
        entries from multiple domains. This API retrieves all the
        domains from which your Directory Sync Service instance is
        configured to read entries. Domains are identified in both DNS
        and distinguished name format.

        Args:
            **kwargs: Supported :meth:`~pancloud.httpclient.HTTPClient.request` parameters.

        Returns:
            requests.Response: Requests Response() object.

        Examples:
            Coming soon.

        """
        path = "/directory-sync-service/v1/domains"
        r = self._httpclient.request(
            method="GET",
            path=path,
            url=self.url,
            **kwargs
        )
        return r

    def query(self, object_class=None, json=None, **kwargs):  # pragma: no cover
        """Query data stored in directory.

        Retrieves directory data by querying a Directory Sync Service
        cloud-based instance. The directory data is stored with the
        Directory Sync Service instance using an agent that is installed
        in the customer's network.This agent retrieves directory data
        from the customer's Active Directory, and then sends it to the
        cloud-based Directory Sync Service instance.

        Args:
            object_class (str): Directory object class.
            json (dict): Payload/request body.
            **kwargs: Supported :meth:`~pancloud.httpclient.HTTPClient.request` parameters.

        Returns:
            requests.Response: Requests Response() object.

        Examples:
            Coming soon.

        """
        path = "/directory-sync-service/v1/{}".format(object_class)
        r = self._httpclient.request(
            method="POST",
            url=self.url,
            json=json,
            path=path,
            **kwargs
        )
        return r
