Django commenting review
========================

*Review of Django commenting apps/frameworks*

+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
|                             | **Extends**    | **Comments**                                                | **Worth**          |
|                             |                |                                                             | **Considering?**   |
|                             | **django-**    |                                                             | [3]_               |
|                             | **contrib-**   |                                                             |                    |
|                             | **comments**   |                                                             |                    |
|                             |                |                                                             |                    |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-contrib-comments_    |   N/A          | Formerly included in Django core, now maintained outside of |  Yes               |
|                             |                | core.                                                       |                    |
|                             |                | Many other commenting apps are based on this package; they  |                    |
|                             |                | typically add "advanced" features like AJAX, threading, etc.|                    |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-threadedcomments_    |   Yes [1]_     | Adds threaded commenting.                                   |  Yes               |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-comments-xtd_        |   Yes          | Adds threaded commenting, follow up notifications & comment |  Yes               |
|                             |                | confirmation by email.                                      |                    |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-fluent-comments_     |   Yes          | Adds AJAX. Included with django-fluent CMS but can be used  |  Maybe?            |
|                             |                | independently.                                              |                    |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| dialogos_                   |   No           | Made by `Eldarion <http://eldarion.com/>`_                  |  Maybe?            |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-richcomments_        |   Yes          | Adds AJAX. Made by `Praekelt <http://www.praekelt.com/>`_   |  Probably not      |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-disqus_              |   No [2]_      |                                                             |  No                |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
| django-ajaxcomments_        |   No           | Adds AJAX, deprecated.                                      |  No                |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
|                             |                |                                                             |                    |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+
|                             |                |                                                             |                    |
+-----------------------------+----------------+-------------------------------------------------------------+--------------------+

Downloads
~~~~~~~~~

Downloads give some indication of the popularity of an app. If you believe that, then `django-threadedcomments <https://github.com/HonzaKral/django-threadedcomments>`_ "wins". However most of its downloads occurred prior to being based on django-contrib-comments, which makes django-comments-xtd the "winner"; followed by django-richcomments, dialogos and django-fluent-comments.


django-threadedcomments
+++++++++++++++++++++++
::

    django-threadedcomments-0.5.1.tar.gz    2009-03-31        4,497
    django-threadedcomments-0.5.2.tar.gz    2009-11-30       12,963
    django-threadedcomments-0.5.3.tar.gz    2010-09-16       12,246
    django-threadedcomments-0.9.0.tar.gz    2013-05-15        5,037
    ---------------------------------------------------------------
    django-threadedcomments has been downloaded 34,743 times!

django-comments-xtd
+++++++++++++++++++++++
::

    django_comments_xtd-1.0a5-py2.6.egg    2012-05-28        1,431
       django-comments-xtd-1.0a5.tar.gz    2012-05-28        1,457
    django_comments_xtd-1.1a1-py2.7.egg    2012-10-17        1,253
       django-comments-xtd-1.1a1.tar.gz    2012-10-17        1,545
    django_comments_xtd-1.2a1-py3.2.egg    2013-06-05          752
       django-comments-xtd-1.2a1.tar.gz    2013-06-05        1,907
     django_comments_xtd-1.2f-py2.7.egg    2014-01-10          608
        django-comments-xtd-1.2f.tar.gz    2014-01-10          665
    django_comments_xtd-1.2f1-py2.7.egg    2014-02-05          583
       django-comments-xtd-1.2f1.tar.gz    2014-02-05          723
      django_comments_xtd-1.2-py3.3.egg    2014-03-02          505
         django-comments-xtd-1.2.tar.gz    2014-03-02          664
       django-comments-xtd-1.3a1.tar.gz    2014-03-04          695
    --------------------------------------------------------------
    django-comments-xtd has been downloaded 12,788 times!

dialogos
+++++++++++++++++++++++
::

    dialogos-0.1.tar.gz    2012-06-07        2,457
    dialogos-0.2.tar.gz    2012-11-01        7,228
    dialogos-0.3.tar.gz    2013-02-12        1,193
    dialogos-0.4.tar.gz    2013-11-27        1,530
    ----------------------------------------------
    dialogos has been downloaded 12,408 times!

django-richcomments
+++++++++++++++++++++++
::

    django_richcomments-0.0.1-py2.6.egg    2010-08-03        1,990
    django_richcomments-0.0.1-py2.5.egg    2010-08-03        1,725
       django-richcomments-0.0.1.tar.gz    2010-08-03        1,665
    django_richcomments-0.0.2-py2.7.egg    2011-09-15        2,120
    django_richcomments-0.0.2-py2.6.egg    2011-09-15        1,767
       django-richcomments-0.0.2.tar.gz    2011-09-15        1,936
    --------------------------------------------------------------
    django-richcomments has been downloaded 11,203 times!

django-fluent-comments
+++++++++++++++++++++++
::

    django-fluent-comments-0.8.0.tar.gz    2013-01-06        1,329
      django-fluent-comments-0.9.tar.gz    2013-05-16          748
    django-fluent-comments-0.9.1.tar.gz    2013-05-28          698
    django-fluent-comments-0.9.2.tar.gz    2013-07-04        2,699
    django-fluent-comments-1.0a1.tar.gz    2014-04-03          463
    django-fluent-comments-1.0a2.tar.gz    2014-04-17          493
    --------------------------------------------------------------
    django-fluent-comments has been downloaded 6,430 times!

django-contrib-comments
+++++++++++++++++++++++
::

    django-contrib-comments-1.5.tar.gz    2013-03-11        5,142
    -------------------------------------------------------------
    django-contrib-comments has been downloaded 5,142 times!


Sources
-------

.. Note:: Forum software was not considered e.g. https://www.djangopackages.com/grids/g/forums/

- https://www.djangopackages.com/grids/g/commenting/

.. _django-contrib-comments: https://github.com/django/django-contrib-comments
.. _django-threadedcomments: https://github.com/HonzaKral/django-threadedcomments 
.. _django-comments-xtd: https://github.com/danirus/django-comments-xtd
.. _django-fluent-comments: https://github.com/edoburu/django-fluent-comments
.. _dialogos: https://github.com/eldarion/dialogos
.. _django-richcomments: https://github.com/praekelt/django-richcomments
.. _django-disqus: https://github.com/arthurk/django-disqus
.. _django-ajaxcomments: https://bitbucket.org/bkonkle/django-ajaxcomments

.. [1] As of 0.9
.. [2] But it will export them to Disqus.
.. [3] Based on a client's req for "in house" commenting system.
