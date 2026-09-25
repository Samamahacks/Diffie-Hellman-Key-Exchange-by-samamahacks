"""
Interactive Diffie-Hellman Key Exchange
Educational implementation.
"""


class DiffieHellman:
    def __init__(self, prime: int, generator: int, private_key: int):
        self.prime = prime
        self.generator = generator
        self.private_key = private_key

        self._validate_parameters()

    def _validate_parameters(self) -> None:
        if self.prime <= 2:
            raise ValueError("Prime must be greater than 2.")

        if not 1 < self.generator < self.prime:
            raise ValueError(
                "Generator must be greater than 1 and less than prime."
            )

        if not 1 < self.private_key < self.prime:
            raise ValueError(
                "Private key must be greater than 1 and less than prime."
            )

    def generate_public_key(self) -> int:
        """
        Public Key = g^private_key mod p
        """
        return pow(self.generator, self.private_key, self.prime)

    def generate_shared_secret(self, other_public_key: int) -> int:
        """
        Shared Secret = other_public_key^private_key mod p
        """
        if not 1 < other_public_key < self.prime:
            raise ValueError("Invalid public key.")

        return pow(
            other_public_key,
            self.private_key,
            self.prime
        )


def get_integer(message: str) -> int:
    """Safely get an integer from the user."""

    while True:
        try:
            return int(input(message))
        except ValueError:
            print(" Please enter a valid integer.")


def main() -> None:
    print("=" * 45)
    print("       DIFFIE-HELLMAN KEY EXCHANGE")
    print("=" * 45)

    print("\n--- Public Parameters ---")

    prime = get_integer("Enter prime number (p): ")
    generator = get_integer("Enter generator (g): ")

    print("\n--- Alice ---")
    alice_private = get_integer("Enter Alice's private key: ")

    print("\n--- Bob ---")
    bob_private = get_integer("Enter Bob's private key: ")

    try:
        # Create Alice and Bob
        alice = DiffieHellman(
            prime,
            generator,
            alice_private
        )

        bob = DiffieHellman(
            prime,
            generator,
            bob_private
        )

        # Generate public keys
        alice_public = alice.generate_public_key()
        bob_public = bob.generate_public_key()

        # Generate shared secrets
        alice_secret = alice.generate_shared_secret(
            bob_public
        )

        bob_secret = bob.generate_shared_secret(
            alice_public
        )

        print("\n" + "=" * 45)
        print("              RESULTS")
        print("=" * 45)

        print(f"\nPublic Prime (p):       {prime}")
        print(f"Generator (g):          {generator}")

        print(f"\nAlice Private Key:      {alice_private}")
        print(f"Alice Public Key:       {alice_public}")

        print(f"\nBob Private Key:        {bob_private}")
        print(f"Bob Public Key:         {bob_public}")

        print(f"\nAlice Shared Secret:    {alice_secret}")
        print(f"Bob Shared Secret:      {bob_secret}")

        print("\n" + "-" * 45)

        if alice_secret == bob_secret:
            print(" Key Exchange Successful!")
            print(f" Shared Secret: {alice_secret}")
        else:
            print(" Key Exchange Failed!")

        print("-" * 45)

    except ValueError as error:
        print(f"\n Error: {error}")


if __name__ == "__main__":
    main()
