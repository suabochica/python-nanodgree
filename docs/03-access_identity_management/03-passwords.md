# Passwords

From a developer's point of view, password is the worst authentication method. In this lesson, we will talk about topics related to password:

- Problems with plain text
- Problems - Brute force attacks
- Problems - Data handling and logging
- Introduction to encryption
- Using encryption for user tables
- Asymmetric encryption
- Hashing
- Hashing with salts

## Problems with Plain Text

Transmitting and storing information such as passwords in plain text is risky because this information is  not guaranteed to be secret forever.

There are many things that can go wrong with the information stored in a database.

- Bad actors
- Bad database passwords
- Bad backup security
- SQL injection

Additionally, there are risks within the API server.

- Bad actors
- Bad logging
- Bad ORM/Serializers

Plain text password also exposes us to risks for data that in-flight between services.

- Intercepted traffic
- "Hotel" WIFI

## SQL injection

SQL injection is a common technique that compromises the data within the database. The SQL injection attacks happen when an un-sanitized HTML input allows a user from the front end to directly request information from the database through the API server.

There are ways to mitigate SQL injection attacks.

- Always validate inputs
- Always sanitize inputs
- Use Object Relational Maps
- Use prepared SQL statements

## Brute Force Attacks

In theory, a user can submit millions or thousands of login requests and they may guess the passwords correctly at some point. This attack is known as a brute force attack.

We can easily mitigate brute force attacks using a few techniques:

- Prevent or ratelimit multiple incorrect login attempts
- Do not allow common passwords
- Enforce a reasonable password policy
- Log and monitor for attack

### An Alternative to Rate-Limiting: CAPTCHAs

Sometimes, rate-limiting or rejecting multiple requests is not the solution. One unintended consequence, for example, would be locking a legitimate user's account because it is under attack. An alternative is something known as a CAPTCHA(opens in a new tab) or "completely automated public Turing test to tell computers and humans apart". A CAPTCHA is designed to be easy for a human but difficult for a machine. In this instance, a connection is flat out rejected if a "bot" or script is attempting to gain access through multiple attempts.

Until recently this was most commonly performed by asking a user to type some form of difficult to read text into an input. But, this problem is adversarial, and with advances in computer vision, these were defeated by scripts. One modern implementation of this system that can be added to your site is Google reCAPTCHA(opens in a new tab). This API produces a score from 0 to 1 of how likely the visitor is a bot based interactions with your site.

## Data Handling and Logging

### Serialization

Serialization is the process of transforming a data model into a more easily shared format. For example, this is commonly performed when sending information as a response from a server to the requesting client in the form of a JSON object.

Logs help us with security for many reasons.

- Logging leaves a solid audit trail
    - Login attempts (ids)
    - Login sources
    - Requested resources

But we should never log:

- Personally identifiable information
- Secrets
- Passwords

You should consider your logs as sensitive data that should be held to the same level of security as the information you are storing in your database tables.

## Encryption

One alternative to password is encryption. Encryption is designed to scramble texts in a predictable fashion and it should also be reversible.

The most basic form of encryption is called simple substitution. We take a keyword and remove each letter of the keyword from the alphabet and shift letters accordingly. Simple substitution ciphers however are very easy to crack.

Polyalphabetic cipher is a simple substitution cipher multiplied by n. However, it is also crackable using some computer assistance.

There are four main parts to use encryption in practice:

- Plaintext block: input data
- Ciphertext block: output from the function
- Function: the algorithm used to perform the encryption
- Key: the cipher

Three common encryption algorithms are:

- 3DES (Data Encryption Standard)
- Blowfish
- AES (Advanced Encryption Standard)

These algorithms works rely on a block cipher such as the **Feistel block cipher**. In Feistel block cipher, the original plaintext is split into two parts, A and B. A passes through a function that uses one of the keys to jumble that text and is then concatenated with the other half of our original plaintext B. That concatenated text is again passing through a function with a key and is then concatenated again with the output from the first stage. This process is repeated many times and finally, we will have a cyphertext block that is very difficult to crack.

It's important that the key is kept secret and is kept. If we lose our key, we can no longer decrypt the information.

### Using Encryption

Encryption can minimize risk if data is compromised because the individual also needs the encryption key to decrypt the message.

However, the key doesn't eliminate all the risks.

- Bad actors
- Bad logging
- Bad ORM/Serializers

Python has a useful package called **Cryptography** that implements encryption for us. We've given you some example code in a notebook below and enough information to answer the questions following the notebook. If you get stuck, refer to the package documentation(opens in a new tab).

### Asymmetric Encryption

One risk we are facing is the messages that are being sent between services because the messages could be read in transit by an attacker.

A more complicated form of encryption is known as asymmetric encryption. In asymmetric encryption, we have more than one key - one private key to encrypt data and one public key to decrypt the data. The private key is kept secret and the public key is given to a different service to decrypt the data.

## Hashing

Hashing is a one-way function that jumbles in only one direction. Compared to encryption, hashing eliminates the key and eliminates the ability to go backwards to the original string.

Some common hashing functions are:

- bcrypt
- scrypt
- ~sha-1~
- ~MD5~

The output from the hashing function is called a hash or a message digest.

Now when we compare passwords, we pass the password submitted by the user to the hashing function and compare the hashes directly.

Although we can't trace back the password using hashing, it doesn't mean hashing is entirely secure. A **rainbow table** is an attack that hashes commonly used passwords and generates the hash-password key-value pair. Once it is generated, we can go through the list of hashes and find the corresponding hash in the rainbow table and trace it back to the user password.

Python has a useful package called **hashlib** that implements MD5 hashing for us. We've given you some example code in a notebook below and enough information to answer the questions following the notebook. If you get stuck, refer to the package documentation(opens in a new tab).

### Hashing with Salts

In this concept we briefly mention Salt Rounds. This is a cost factor for how many times a password and salt should be re-hashed. In other words if you choose 10 salt rounds, the calculation is performed 2^10 or 1024 times. Each attempt takes the hash from the previous round as an input. The more rounds performed, the more computation is required to compute the hash. This will not cause significant time for a single attempt (i.e. checking a password at login), but will introduce significant time when attempting to brute force or generate rainbow tables.

Python has a useful package called **BCrypt** that implements the BCrypt hashing algorithm as well as random salt generation for us. We've given you some example code in a notebook below and enough information to answer the questions following the notebook. If you get stuck, refer to the package documentation(opens in a new tab).

## Recap

In this lesson, we answered the question of why passwords are unreliable and discussed some of the methods to minimize the risk of using passwords.

Here is a list of topics we talked about in the lesson.

- Problems with plain text
- Problems - Brute force attacks
- Problems - Data handling and logging
- Introduction to encryption
- Using encryption for user tables
- Asymmetric encryption
- Hashing
- Hashing with salts

