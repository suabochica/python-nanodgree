# Thinking Adversarially

In this section, we will explore some common techniques used by adversaries to attack our infrastructure and gain access to data that they should not have access to.

The topics we will talk about are:

- Limiting access to code and systems
- Code review for security
- Auth validation testing
- Alternative attack vectors
- Staying ahead of the attackers

## Using Git

Git is a tool used by developers to keep track of changes and ensure that their code is a single source for other developers to work on.

Committing to master causes problems because we might have conflicting versions or conflicting code across the system. In addition, mirroring production data causes problems because it opens up to undue risks.

There are some actions that we can take to ensure the system is secure and in sync.

- Replicating the data store locally and using fake data to simulate what the system will look like in production. This can eliminate the risk of having the data compromised locally.
- Using different branches while developing and using staging branch to verify changes. This can minimize the risks of being out of sync in software.

By using the above techniques, we can have a clear state and segmented data. In addition, we can protect specific branches so only trusted individuals can interact with the code contained within. We can also implement a code review process in which a peer engineer will review the code before a pull request is committed.

In Github repo, we can create new branches like staging and dev. We can also change the default branch to dev We can also add protection rules to prevent unauthorized commits to the protected branches.

## Limiting Credentials

The principles learned in this course should also be applied to the systems you consume as a developer. You want to ensure that the systems you're building are secure and cannot be changed without trusted individuals vetting those changes. After all, code review is effectively useless if the individual requesting the review can simply bypass the check and push their code directly to the production server. Take a moment to reflect on how you would configure credentials for a new junior engineer

## Code Review as Security tool

Only approved code can be merged to the master branch. This process ensures that no vulnerable code is elevated to the master deployment.

## Auth Validation Testing

Integration test and unit tests are automated scripts that ensure that the output of the function do what they are supposed to do. We can implement integration tests using Postman. For example:

```js
pm.test("Status code is 401", function () {
  pm.response.to.have.status(401);
});
```

We can aggregate tests together into a Postman collection. We do this by saving the request in a single folder and run an entire collcection in Collection Runner.

**Penetration testing** means that we hire a hacker to attack our system and tell us which points are most vulnerable

## Alternate Attack Vectors

### Phishing

**Phishing** refers to an attacker obtaining information by pretending to be someone else. Most phishing attacks are conducted over email, but there are more sophisticated phishing attacks that people easily fall such as cloning an entire sign-in page.

### Social Engineering

**Social engineering** is another common attack technique. This is an attack where an attacker might know your information or find information that's publicly available to attack your system.

## Staying Ahead of the Attackers

The landscape of how attackers gain access to systems is always changing and we need to stay ahead to make sure our systems are secure. One way to do it is by reading the news, checking security blogs and websites, and subscribe to the information security feed.

### OWASP Top 10

Open Web Application Security Project or OWASP Top 10 is a list of the 10 most common vulnerabilities for web applications. It is a good resource to keep yourself updated about information security.

### Subscribring to Vulnerability Monitoring

The last area we should focus on is the other tools, services, or dependencies that we are using. When we sign up for new services or make new software decisions, we should ask ourselves security questions such as

- How is data stored? Is it encrypted?
- How is data destroyed?
- Do they use secure 3-rd parties?
- Who has access?
- Do they have any certifications?

## Recap

Congratulations on completing the course. In this final lesson, we talked about:

- Limiting access to code and systems
- Code review for security
- Auth validation testing
- Alternative attack vectors
- Staying ahead of the attackers

Throughout the course, you have learned how to identify who is making requests to our service using a third-party authentication service and JWT. We also explored why password with plain text is absolutely the worst and how to mitigate the risks with passwords. We also covered how to define roles and permissions to restrict certain actions to certain users. Finally, we learned that we should always stay ahead of attackers to continuing to protect our systems.
