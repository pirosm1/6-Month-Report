#!/usr/bin/env python3
import os
import argparse
import subprocess
from operator import itemgetter

# find top 10 contributors
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Top 10 contributors of brew")

    parser.add_argument("year",
                        metavar="<year>",
                        type=int,
                        help="Year to take stats from")

    args = parser.parse_args()

    result = subprocess.run(["git", "--no-pager", "log", "--no-merges",
                             "--shortstat", "--pretty=format:%an",
                             "--after='{0}-01-01'".format(args.year),
                             "--before='{0}-07-01'".format(args.year)],
                             stdout=subprocess.PIPE)

    string_result = result.stdout.decode("utf-8")
    lines = string_result.split(os.linesep)
    lines = list(filter(None, lines))     # remove empty strings from lines

    person_dict = {}

    line_index = 0
    while (line_index != len(lines)):
        # grab name
        name = lines[line_index]
        line_index = line_index + 1

        # grab contribution string
        contribution_str = lines[line_index]
        # grab integers from contribution_string
        contribs = [int(s) for s in lines[line_index].split() if s.isdigit()]
        line_index = line_index + 1

        files_changed = contribs[0]     # files_changed is always first
        insertions = 0
        deletions = 0
        if '+' in contribution_str and '-' in contribution_str:
            # both insertions and deletions in the contribution string
            insertions = contribs[1]
            deletions = contribs[2]
        elif '+' in contribution_str:
            # just insertions in contribution string
            insertions = contribs[1]
        else:
            # just deletions in contribution string
            deletions = contribs[1]

        try:
            person_dict[name]["files_changed"] = person_dict[name]["files_changed"] + files_changed
            person_dict[name]["insertions"] = person_dict[name]["insertions"] + insertions
            person_dict[name]["deletions"] = person_dict[name]["deletions"] + deletions
            person_dict[name]["nonmerged_commits"] = person_dict[name]["nonmerged_commits"] + 1
        except KeyError as err:
            # Person doesn't exist yet
            person_dict[name] = {
                "files_changed": files_changed,
                "insertions": insertions,
                "deletions": deletions,
                "nonmerged_commits": 1
            }

    person_list = []
    for key, value in person_dict.items():
        person_list.append({
            "name": key,
            "files_changed": value["files_changed"],
            "insertions": value["insertions"],
            "deletions": value["deletions"],
            "nonmerged_commits": value["nonmerged_commits"]
        })

    print("First 6 months report for {0}\n".format(args.year))
    print("Name\t\t\t| Files Changed\t| Insertions\t| Deletions\t| Commits\n")
    person_list = sorted(person_list, key=itemgetter("insertions"), reverse=True)
    for person in person_list[:10]:
        print("{0}\t\t| {1}\t\t| {2}\t\t| {3}\t\t| {4}".format(
            person["name"],
            person["files_changed"],
            person["insertions"],
            person["deletions"],
            person["nonmerged_commits"]))