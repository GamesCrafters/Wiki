Wiki Cleanup
============

Overview
========

Within the last year, the Gamesman Wiki has been infiltrated by spam bots that create bogus wiki pages with links to commercial websites. The goal of this project is to clean up the spam and unnecessary pages and ban the spam bots while preserving all of the legitimate information.

How it Started
--------------

The project started at the beginning of the Spring 2009 semester as a part of the enhanced wiki documentation initiative. (See the [Checklist Information](Checklist_Information "wikilink") page) The unhealthy state of the wiki was first brought to the attention of the group in the second week of instruction. Since the wiki is viewed as the central resource for all of the Gamesman information, it seemed to be a good idea to make the cleanup task part of the same project.

Current Status
--------------

The project remains in its infancy. Currently only minor steps have been taken including installing a spam sweeper that checks for spam weblinks embedded in wiki pages and a captcha system that makes it more difficult for automated spam bots to create accounts. Far more work can and should be done on this project, although performing the job efficiently it may require more detailed knowledge of PHP and databases then was previously thought. (Both of which the project founder lacked)

Installed Components
====================

Spam Sweeper
------------

The spam sweeper takes in spam urls in a huge regular expression and then checks each page on the wiki for matches to those links. If one is found on a page, the sweeper attempts to revert the page back to the last version that did not contain any mention of spam weblinks. If no clean revision can be found, the page is deleted.

Captcha
-------

A captcha system has been partially installed. The current configuration forces those signing up for new accounts to answer a grade-school level math question before being given an account. With the proper libraries, this can be upgraded to a visual password captcha. (See the problems section)

Password Enforced Account Signup
--------------------------------

Problems
========

Access Privileges
-----------------

The wiki cleanup project code is somewhat less accessible than other Gamesman projects. Other projects are kept in public source control repositories and can be checked out by anyone that is interested. The wiki code, however, is kept entirely on the nyc web server and is available only via root access.

While this can be obtained under the supervision of the class instructor and web team leads, administrator access to the wiki itself is a bit more difficult to acquire. Some of the more straight foreword methods of enforcing user bans and deleting pages require admin or bureaucrat wiki account status which can only be granted by someone that already has that rank. There are three admin/bureaucrats listed on the wiki user list under the aliases of Admin, Ide, and Seancarr. Of the three, Seancarr is the only one that has a non-empty user page, while none of them have any contact information. Without direct administrative authority, wiki maintenance becomes a bit more problematic as all deletions and bans must be done without the aid of the wiki front-end.

Spam Sweeper: Manual Configuration
----------------------------------

The spam sweeper does its job well. However, each link that it is to label as spam must be added to its blacklist manually. This is not only time consuming but also terribly inefficient. Adding a url to the blacklist will sweep all pages with that link embedded in them. It may delete one hundred pages, fifty pages, or a single page depending on how many pages contain the same url. On average, adding a link seems to delete about five pages. With a problem as severe as the Gamesman wiki this is not a serious advantage. The problem becomes more serious when one takes into account the fact that the spam on the Gamesman wiki is very specialized towards things like online game currency exchange. Thus, the spam links on the Gamesman Wiki are not found on the more general blacklists and must be added manually.

Lastly, there are many pages that obviously contain spam, but do not contain any links. The spam sweeper operates by looking for links, and therefore will ignore these pages. Thus, the spam sweeper can not clean the wiki alone, but can only be considered a tool to help keep the wiki clean.

Captcha
-------
