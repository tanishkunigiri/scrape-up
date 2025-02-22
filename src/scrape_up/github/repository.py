import requests
from bs4 import BeautifulSoup

import requests_html
import os


class Repository:
    def __init__(self, username: str, repository_name: str):
        self.username = username
        self.repository = repository_name

    def __str__(self):
        return f"{self.repository} belongs to {self.username}"

    def __scrape_page(self):
        data = requests.get(f"https://github.com/{self.username}/{self.repository}")
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_tags_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/tags"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_issues_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/issues"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_pull_requests_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/pulls"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_deployments_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/deployments/activity_log"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def __scrape_watchers_page(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/watchers"
        )
        data = BeautifulSoup(data.text, "html.parser")
        return data

    def languagesUsed(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        languagesUsed = repository.languagesUsed()
        ```
        Returns:
        {
        "data": allLanguages,
        "message": f"Languages used in {self.repository} repository",
        }
        """
        data = self.__scrape_page()

        try:
            languages = data.find_all(class_="color-fg-default text-bold mr-1")
            allLanguages = []
            for item in languages:
                item = str(item)
                item = item[46:]
                item = item[:-7]
                allLanguages.append(item)
            # return allLanguages  # return list of languages
            return {
                "data": allLanguages,
                "message": f"Languages used in {self.repository} repository",
            }
        except:
            message = f"No languages found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def about(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        about = repository.about()
        ```
        Returns:
        {
        "data": about,
        "message": f"About {self.repository} repository",
        }
        """
        data = self.__scrape_page()

        try:
            tag = data.find(class_="f4 mb-3")
            about = tag.get_text()
            return {
                "data": about,
                "message": f"About {self.repository} repository",
            }
        except:
            message = (
                f"No details found in the about section of {self.repository} repository"
            )
            return {
                "data": None,
                "message": message,
            }

    def fork_count(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        fork_count = repository.fork_count()
        ```
        Returns:
        {
        "data": fork_count,
        "message": f"Number of forks of {self.repository} repository",

        }
        """
        data = self.__scrape_page()
        try:
            stats_body = data.find(
                "ul", class_="pagehead-actions flex-shrink-0 d-none d-md-inline"
            )
            forks = stats_body.find("span", id="repo-network-counter")
            fork_count = forks.text.strip()
            return {
                "data": fork_count,
                "message": f"Number of forks of {self.repository} repository",
            }
        except:
            message = f"No forks found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def topics(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        topics = repository.topics()
        ```
        Returns:
        {
        "data": allTopics,
        "message": f"Topics of {self.repository} repository",
        }
        """
        data = self.__scrape_page()

        try:
            topics = data.find_all(class_="topic-tag topic-tag-link")
            allTopics = []
            print(allTopics)
            for item in topics:
                allTopics.append(item.text)
            return {
                "data": allTopics,
                "message": f"Topics of {self.repository} repository",
            }
        except:
            message = f"No topics found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def star_count(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        star_count = repository.star_count()
        ```
        Returns:
        {
        "data": starCount,
        "message": f"Star count of {self.repository} repository",
        }
        """
        try:
            data = self.__scrape_page()
            starCount = (
                data.find("a", href=f"/{self.username}/{self.repository}/stargazers")
                .find("span")
                .text.strip()
            )
            return {
                "data": starCount,
                "message": f"Star count of {self.repository} repository",
            }
        except:
            message = f"No stars found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def pull_requests(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        pull_requests = repository.pull_requests()
        ```
        Returns:
        {
        "data": pull_requests,
        "message": f"Pull requests of {self.repository} repository",
        }
        """
        data = self.__scrape_page()
        try:
            pull_requests = (
                data.find_all(class_="UnderlineNav-item mr-0 mr-md-1 mr-lg-3")[2]
                .find_all("span")[1]
                .text.strip()
            )
            return {
                "data": pull_requests,
                "message": f"Pull requests of {self.repository} repository",
            }
        except:
            message = f"No pull requests found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def tags(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        tags = repository.tags()
        ```
        Returns:
        {
        "data": allTags,
        "message": f"Tags of {self.repository} repository",
        }
        """
        data = self.__scrape_tags_page()
        try:
            tags = data.find_all(class_="Link--primary")
            allTags = []
            for item in tags:
                allTags.append(item.text)
            return {
                "data": allTags,
                "message": f"Tags of {self.repository} repository",
            }
        except:
            message = f"No tags found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def releases(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        releases = repository.releases()
        ```
        Returns:
        {
        "data": allReleases,
        "message": f"Releases of {self.repository} repository",
        }
        """
        data = self.__scrape_tags_page()
        try:
            releases = data.find_all(class_="Link--primary")
            allReleases = []
            for item in releases:
                allReleases.append(item.text)
            return {
                "data": allReleases,
                "message": f"Releases of {self.repository} repository",
            }
        except:
            message = f"No releases found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def issues_count(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        issues_count = repository.issues_count()
        ```
        Returns:
        {
        "data": issues,
        "message": f"Total issues in {self.repository} repository",
        }
        """
        data = self.__scrape_page()
        try:
            issues = data.find("span", {"id": "issues-repo-tab-count"}).text.strip()
            return {
                "data": issues,
                "message": f"Total issues in {self.repository} repository",
            }
        except:
            message = f"No issues found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def readme(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        readme = repository.readme()
        ```
        Returns:
        {
         message = f"No readme found in {self.repository} repository"
        }
        """
        session = requests_html.HTMLSession()
        r = session.get(
            f"https://github.com/{self.username}/{self.username}/blob/main/README.md"
        )
        markdown_content = r.text

        try:
            with open("out.md", "w", encoding="utf-8") as f:
                f.write(markdown_content)
        except:
            message = f"No readme found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def get_pull_requests_ids(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_pull_requests_ids = repository.get_pull_requests_ids()
        ```
        Returns:
        {
        "data": pull_requests_ids,
        "message": f"Pull requests of {self.repository} repository",
        }
        """
        data = self.__scrape_pull_requests_page()
        try:
            pr_body = data.find(
                "div", class_="js-navigation-container js-active-navigation-container"
            )
            pull_requests_ids = []
            for each_pr in pr_body.find_all(
                "a",
                class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title",
            ):
                pr_id = each_pr["href"].split("/")[-1]
                pull_requests_ids.append(pr_id)

            return {
                "data": pull_requests_ids,
                "message": f"Pull requests of {self.repository} repository",
            }
        except:
            message = f"No pull requests found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def commits(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        commits = repository.commits()
        ```
        Returns:
        {
        "data": commits,
        "message": f"Commits of {self.repository} repository",
        }
        """
        data = self.__scrape_page()
        try:
            commits = str(data.find_all(class_="d-none d-sm-inline"))
            s = commits.split("<strong>")
            s = s[1].split("</strong>")
            commits = int(s[0])
            return {
                "data": commits,
                "message": f"Commits of {self.repository} repository",
            }
        except:
            message = f"No commits found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def get_issues(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_issues = repository.get_issues()
        ```
        Returns:
        {
        "data": allIssues,
        "message": f"Issues of {self.repository} repository",
        }
        """
        data = self.__scrape_issues_page()
        try:
            issues = data.find_all(
                class_="Link--primary v-align-middle no-underline h4 js-navigation-open markdown-title"
            )
            allIssues = []

            for item in issues:
                allIssues.append(item.text)
            return {
                "data": allIssues,
                "message": f"Issues of {self.repository} repository",
            }
        except:
            message = f"No issues found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def get_contributors(self):
        data = self.__scrape_page()

        try:
            contributors = data.find_all(
                "a", href=f"/{self.username}/{self.repository}/graphs/contributors"
            )
            contributor = []
            for it in contributors:
                contributor.append(it.get_text())
            return {
                "data": contributor[0].strip(),
                "message": f"Contributors of {self.repository} repository",
            }
        except:
            message = f"No contributors found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def last_update_at(self):
        data = self.__scrape_page()
        try:
            update = data.find_all("relative-time", class_="no-wrap")
            return {
                "data": update[0].get_text(),
                "message": f" last Updated of {self.repository} repository",
            }
        except:
            message = f"No updation found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def get_readme(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_readme = repository.get_readme()
        ```
        Returns:
        {
        "data": None,
        "message": message,
        }
        """
        data = requests.get(
            f"https://raw.githubusercontent.com/{self.username}/{self.username}/master/README.md"
        )
        if data.status_code == 404:
            data = requests.get(
                f"https://raw.githubusercontent.com/{self.username}/{self.username}/main/README.md"
            )
            if data.status_code == 404:
                message = f"No special repository found with username {self.username}"
                return {
                    "data": None,
                    "message": message,
                }
        else:
            path = f"./{self.username}"
            try:
                os.mkdir(path)
            except OSError as error:
                return error
            data = data.text
            readmeFile = os.open(path + "/README.md", os.O_RDWR | os.O_CREAT)
            os.write(readmeFile, data.encode("utf-8"))
            message = "README.md found & saved"
            return message

    def get_environment(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        get_environment = repository.get_environment()
        ```
        Returns:
        {
        "data": link,
        "message": f"Latest enviornment link for {self.repository} is {link}",
        }
        """
        try:
            data = self.__scrape_deployments_page()
            link = data.find(
                "a", class_="btn btn-outline flex-self-start mt-2 mt-md-0"
            ).get("href")
            return {
                "data": link,
                "message": f"Latest enviornment link for {self.repository} is {link}",
            }
        except:
            message = f"No link found for {self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def get_branch(self):
        data = requests.get(
            f"https://github.com/{self.username}/{self.repository}/branches"
        )
        data = BeautifulSoup(data.text, "html.parser")
        try:
            branch = data.find_all(
                class_="branch-name css-truncate-target v-align-baseline width-fit mr-2 Details-content--shown"
            )
            allBranches = []
            for branchNames in branch:
                allBranches.append(branchNames.text.strip())
            return {
                "data": allBranches,
                "message": f"The branches of {self.repository}/{self.username} is {allBranches}",
            }
        except:
            message = f"Failed to fetch branches of {self.username}/{self.repository}"
            return {
                "data": None,
                "message": message,
            }

    def watch_count(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        watch_count = repository.watch_count()
        ```
        Returns:
        {
        "data": watches,
        "message": f"Total watches in {self.repository} repository",
        }
        """
        data = self.__scrape_watchers_page()
        try:
            watches = len(data.find("ol", {"class": "gutter"}).find_all("li"))
            return {
                "data": watches,
                "message": f"Total watches in {self.repository} repository",
            }
        except:
            message = f"No watches found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

    def all_watchers(self):
        """
        Class - `Repository`
        Example:
        ```
        repository = github.Repository(username="nikhil25803", repository_name="scrape-up")
        all_watchers = repository.all_watchers()
        ```
        Returns:
        {
          return watchers
        }
        """
        data = self.__scrape_watchers_page()
        try:
            all = data.find("ol", {"class": "gutter"}).find_all(
                "a", {"data-hovercard-type": "user"}
            )[1::2]
            watchers = []
            for watcher in all:
                watchers.append(watcher.text.strip())
            return watchers

        except:
            message = f"No watchers found in {self.repository} repository"
            return {
                "data": None,
                "message": message,
            }

