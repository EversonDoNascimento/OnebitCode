type Props = {
  value: string;
  label: string;
  id: string;
  setValue: (title: string) => void;
};

export default function TextInput({ id, value, label, setValue }: Props) {
  return (
    <div>
      <label htmlFor={id}>{label}</label>
      <input
        type="text"
        name={id}
        id={id}
        value={value}
        onChange={(e) => {
          setValue(e.target.value);
        }}
      />
    </div>
  );
}
